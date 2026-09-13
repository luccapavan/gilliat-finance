"""
Servidor Local de Landing Pages e Coleta de Leads
Execução simples sem dependências externas:
    python landing_pages/server.py
Acesse:
    http://localhost:8000
"""

import http.server
import socketserver
import json
import csv
from pathlib import Path
from datetime import datetime
import urllib.parse

PORT = 8000
BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "leads.csv"
JSON_FILE = BASE_DIR / "leads.json"

class LeadCaptureHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def do_POST(self):
        if self.path == '/api/leads':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            try:
                lead = json.loads(post_data.decode('utf-8'))
            except Exception:
                # Caso venha urlencoded
                parsed = urllib.parse.parse_qs(post_data.decode('utf-8'))
                lead = {k: v[0] if len(v) == 1 else v for k, v in parsed.items()}

            lead['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # 1. Salvar em CSV
            file_exists = CSV_FILE.exists()
            with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=[
                    'created_at', 'course', 'name', 'email', 'phone', 
                    'role', 'python_level', 'aum', 'availability'
                ])
                if not file_exists:
                    writer.writeheader()
                writer.writerow({
                    'created_at': lead.get('created_at', ''),
                    'course': lead.get('course', ''),
                    'name': lead.get('name', ''),
                    'email': lead.get('email', ''),
                    'phone': lead.get('phone', ''),
                    'role': lead.get('role', ''),
                    'python_level': lead.get('python_level', ''),
                    'aum': lead.get('aum', ''),
                    'availability': lead.get('availability', '')
                })

            # 2. Salvar em JSON acumulado
            leads_list = []
            if JSON_FILE.exists():
                try:
                    with open(JSON_FILE, 'r', encoding='utf-8') as f:
                        leads_list = json.load(f)
                except Exception:
                    leads_list = []
            leads_list.append(lead)
            with open(JSON_FILE, 'w', encoding='utf-8') as f:
                json.dump(leads_list, f, indent=2, ensure_ascii=False)

            print(f"✅ Novo Lead Recebido! [{lead.get('course')}] {lead.get('name')} <{lead.get('email')}> | Horário: {lead.get('availability')}")

            # Responder JSON de sucesso
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {"status": "success", "message": "Lead registrado com sucesso!"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_error(404, "Endpoint not found")

    def do_OPTIONS(self):
        # Suporte a CORS para requisições de outros domínios
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), LeadCaptureHandler) as httpd:
        print("=" * 60)
        print(f"🚀 Servidor de Landing Pages rodando em: http://localhost:{PORT}")
        print(f"📁 Leads serão salvos automaticamente em:")
        print(f"   • {CSV_FILE.name}")
        print(f"   • {JSON_FILE.name}")
        print("=" * 60)
        print("Pressione Ctrl+C para encerrar o servidor a qualquer momento.\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor encerrado.")
