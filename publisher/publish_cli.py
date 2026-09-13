"""
CLI para Gerenciamento e Publicação de Conteúdo no LinkedIn (Suporte Bilíngue PT/EN)
"""
import sys
import os
import json
from pathlib import Path

# Garante suporte completo a UTF-8 e emojis no terminal Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from publisher.buffer_publisher import schedule_via_buffer

def get_posts(batch_num: int = 2):
    batch_str = f"batch_{batch_num:02d}"
    batch_file = Path(f"posts/{batch_str}/index.json")
    if not batch_file.exists():
        batch_file = Path("posts/batch_01/index.json")
        batch_num = 1
        if not batch_file.exists():
            print(f"Nenhum lote gerado para {batch_str}.")
            return [], batch_num
    with open(batch_file, "r", encoding="utf-8") as f:
        return json.load(f), batch_num

def list_posts(batch_num: int = 2):
    posts, actual_batch = get_posts(batch_num)
    print(f"\n==================== Posts Disponíveis no LOTE {actual_batch} (Bilíngue PT/EN) ====================")
    for i, p in enumerate(posts, 1):
        title_pt = p.get("title_pt", p.get("title"))
        title_en = p.get("title_en", "English translation available")
        print(f"[{i}] PT: {title_pt}")
        print(f"    EN: {title_en}")
        print(f"    Pilar: {p['pillar']} | Horário: {p['suggested_day']}")
        print("-" * 75)
    print("Comandos úteis:")
    print("  python publisher/publish_cli.py list [lote]                       -> Listar posts (padrão: 2)")
    print("  python publisher/publish_cli.py view <post_n> [lote] [pt|en]      -> Ver texto do post no idioma")
    print("  python publisher/publish_cli.py queue <post_n> [lote] [pt|en]     -> Agendar na Fila do Buffer")
    print("  python publisher/publish_cli.py draft <post_n> [lote] [pt|en]     -> Enviar como Rascunho para o Buffer")
    print("  python publisher/publish_cli.py share-now <post_n> [lote] [pt|en] -> Publicar AGORA no LinkedIn")
    print("====================================================================================\n")
    return posts

def view_post(post_idx: int, batch_num: int = 2, lang: str = "pt"):
    posts, actual_batch = get_posts(batch_num)
    if 1 <= post_idx <= len(posts):
        post = posts[post_idx - 1]
        lang = lang.lower()
        title = post.get(f"title_{lang}", post.get("title", post.get("title_pt")))
        content = post.get(f"content_{lang}", post.get("content", post.get("content_pt")))
        
        print(f"\n==========================================")
        print(f"LOTE   : {actual_batch} | POST [{post_idx}] | IDIOMA: {lang.upper()}")
        print(f"TITULO : {title}")
        print(f"PILAR  : {post['pillar']}")
        print(f"HORARIO: {post['suggested_day']}")
        print(f"==========================================\n")
        print(content)
        print(f"\n==========================================")
    else:
        print(f"Índice de post inválido: {post_idx}")

def publish_action(post_idx: int, action: str, batch_num: int = 2, lang: str = "pt"):
    posts, actual_batch = get_posts(batch_num)
    if not (1 <= post_idx <= len(posts)):
        print("Índice de post inválido.")
        return
        
    post = posts[post_idx - 1]
    lang = lang.lower()
    title = post.get(f"title_{lang}", post.get("title", post.get("title_pt")))
    content = post.get(f"content_{lang}", post.get("content", post.get("content_pt")))
    
    print(f"\nProcessando Post [{post_idx}] do Lote {actual_batch} em [{lang.upper()}]: '{title}'...")
    
    if action == "draft":
        print("Enviando para a aba de Rascunhos do Buffer (para revisão)...")
        res = schedule_via_buffer(content, mode="addToQueue", save_to_draft=True)
    elif action == "queue":
        print("Agendando na fila oficial do Buffer...")
        res = schedule_via_buffer(content, mode="addToQueue", save_to_draft=False)
    elif action == "share-now":
        print("Disparando publicação IMEDIATA no LinkedIn via Buffer...")
        res = schedule_via_buffer(content, mode="shareNow", save_to_draft=False)
    else:
        print(f"Ação desconhecida: {action}")
        return

    if res.get("success"):
        print(f"[OK] Sucesso! Post ID no Buffer: {res.get('post_id')} (Status: {res.get('status')})")
        print("Acesse https://publish.buffer.com para conferir no calendário!")
    else:
        print(f"[!] Erro ao processar: {res.get('error', res)}")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        list_posts(2)
    else:
        cmd = args[0]
        if cmd == "list":
            b = int(args[1]) if len(args) > 1 else 2
            list_posts(b)
        elif cmd == "view":
            if len(args) > 1:
                p_idx = int(args[1])
                b = int(args[2]) if len(args) > 2 else 2
                l = args[3] if len(args) > 3 else "pt"
                view_post(p_idx, b, l)
            else:
                print("Uso: python publisher/publish_cli.py view <post_n> [lote] [pt|en]")
        elif cmd in ["draft", "queue", "share-now"]:
            if len(args) > 1:
                p_idx = int(args[1])
                b = int(args[2]) if len(args) > 2 else 2
                l = args[3] if len(args) > 3 else "pt"
                publish_action(p_idx, cmd, b, l)
            else:
                print(f"Uso: python publisher/publish_cli.py {cmd} <post_n> [lote] [pt|en]")
        else:
            print("Comando não reconhecido. Use: list, view, draft, queue, share-now.")
