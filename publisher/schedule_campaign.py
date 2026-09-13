import os
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from publisher.buffer_publisher import schedule_via_buffer
from publisher.publish_cli import get_batch_posts

def get_upcoming_slots(num_slots: int):
    """
    Gera os próximos horários disponíveis alternando entre 12:00 e 18:30 (Horário de Brasília - UTC-3).
    12:00 BRT = 15:00:00 UTC
    18:30 BRT = 21:30:00 UTC
    """
    slots = []
    now = datetime.now()
    current_date = now.date()
    
    days_ahead = 0
    while len(slots) < num_slots:
        target_day = current_date + timedelta(days=days_ahead)
        
        # Slot 12:00 BRT (15:00 UTC)
        slot_12 = datetime(target_day.year, target_day.month, target_day.day, 12, 0, 0)
        slot_12_utc = f"{target_day.strftime('%Y-%m-%d')}T15:00:00.000Z"
        if slot_12 > now:
            slots.append((slot_12_utc, f"{target_day.strftime('%d/%m/%Y')} às 12:00 BRT"))
            if len(slots) == num_slots:
                break
                
        # Slot 18:30 BRT (21:30 UTC)
        slot_1830 = datetime(target_day.year, target_day.month, target_day.day, 18, 30, 0)
        slot_1830_utc = f"{target_day.strftime('%Y-%m-%d')}T21:30:00.000Z"
        if slot_1830 > now:
            slots.append((slot_1830_utc, f"{target_day.strftime('%d/%m/%Y')} às 18:30 BRT"))
            if len(slots) == num_slots:
                break
                
        days_ahead += 1
        
    return slots

def run_campaign():
    posts = get_batch_posts()
    if not posts:
        print("Nenhum post encontrado.")
        return

    sequence = [1, 4, 2, 5, 3]
    slots = get_upcoming_slots(len(sequence))
    
    print("\n=======================================================")
    print("[*] INICIANDO AGENDAMENTO DA CAMPANHA NO BUFFER (12:00 & 18:30 BRT)")
    print("=======================================================\n")
    
    scheduled_count = 0
    for i, idx in enumerate(sequence):
        post = posts[idx - 1]
        due_utc, label_brt = slots[i]
        print(f"-> Agendando Post [{idx}] para {label_brt}...")
        res = schedule_via_buffer(post["content"], mode="customScheduled", save_to_draft=False, due_at=due_utc)
        
        if res.get("success"):
            print(f"   [OK] Agendado! Post ID: {res.get('post_id')} (Status: {res.get('status')})")
            scheduled_count += 1
        else:
            print(f"   [!] Erro: {res.get('error', res)}")
            
        time.sleep(1)
        
    print("\n=======================================================")
    print(f"[OK] Campanha agendada com sucesso: {scheduled_count}/{len(sequence)} posts adicionados a fila!")
    print("Acesse https://publish.buffer.com para visualizar os horarios no calendario.")
    print("=======================================================\n")

if __name__ == "__main__":
    run_campaign()
