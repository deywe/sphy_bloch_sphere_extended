from ursina import *
from ursina.prefabs.trail_renderer import TrailRenderer
from ursina.shaders import lit_with_shadows_shader
import pandas as pd
import hashlib

# --- CONFIGURAÇÃO DA ENGINE ---
app = Ursina()

# Definindo a resolução da janela Full HD
window.size = (1920, 1080)
window.position = Vec2(0, 0)
window.title = "SPHY ENGINE - ENTANGLED VALIDATOR"
window.color = color.black

# --- CARREGAMENTO DE DADOS ---
try:
    df = pd.read_parquet('sphy_bloch_data.parquet')
    max_frames = df['frame'].max()
    # Identifica o total de qubits ativos no dataset
    n_qubits = df['qubit_id'].nunique()
except:
    print("Erro: Arquivo sphy_bloch_data.parquet não encontrado!")
    quit()

# --- AMBIENTE ---
nucleus = Entity(model='sphere', texture='shore', scale=5, shader=lit_with_shadows_shader)
bloch_sphere = Entity(model='sphere', color=color.rgba(255, 255, 0, 20), scale=30, double_sided=True)
bloch_sphere.set_render_mode_wireframe()

# TÍTULO SUPERIOR
title = Text(
    text='S(Φ) ENGENIE - REAL BLΟCH SPHERE PRΟCESSOR CHALLENGE',
    position=(0, 0.45), origin=(0,0), scale=1.2, color=color.yellow
)

# DISPLAY DE VALIDAÇÃO (COLUNA ESQUERDA)
status_text = Text(text='', position=(-0.85, 0.42), scale=1.1, color=color.lime)

qubits_entities = []
for i in range(n_qubits):
    # Diferenciação visual por matiz (HSV)
    q = Entity(model='sphere', color=color.hsv(i*(360/n_qubits), 0.7, 1), scale=0.4, shader=lit_with_shadows_shader)
    q.trail = TrailRenderer(parent=q, thickness=0.04, color=q.color, length=40)
    qubits_entities.append(q)

current_frame = 0

def update():
    global current_frame
    
    if current_frame <= max_frames:
        # 1. Isolar dados do frame e ordenar para validação hash
        frame_data = df[df['frame'] == current_frame].sort_values('qubit_id')
        
        # 2. RECONSTRUÇÃO DO PAYLOAD EMARANHADO
        accumulators_list = frame_data['soma_local'].tolist()
        timestamp = frame_data['timestamp'].iloc[0]
        stored_hash = frame_data['sha256'].iloc[0]
        
        raw_payload = f"{current_frame}-{accumulators_list}-{timestamp}"
        recalculated_sha = hashlib.sha256(raw_payload.encode()).hexdigest()
        
        # 3. VALIDAÇÃO DE SOBERANIA
        is_valid = recalculated_sha == stored_hash
        valid_status = "QUANTUM SOVEREIGNTY: OK" if is_valid else "CORE BREACH: CORRUPTED"
        status_color = color.lime if is_valid else color.red
        
        total_soma_sistema = sum(accumulators_list)
        
        # 4. ATUALIZAÇÃO VISUAL DAS ENTIDADES
        for i, q_ent in enumerate(qubits_entities):
            q_row = frame_data.iloc[i] 
            q_ent.position = (q_row['x'], q_row['y'], q_row['z'])
            
        # 5. UI UPDATE (Total Qubits como primeiro da lista)
        status_text.text = (
            f"QUBITS RUNNING NOW: {n_qubits}\n"
            f"FRAME: {current_frame}\n"
            f"TOTAL SYSTEM SPHY: {total_soma_sistema}\n"
            f"STATUS: {valid_status}\n"
            f"HASH: {recalculated_sha[:20]}..."
        )
        status_text.color = status_color
        
        current_frame += 1
    else:
        status_text.text += "\n\n[SIMULATION COMPLETE]"

def input(key):
    if key == 'escape': quit()
    if key == 'space':
        global current_frame
        current_frame = 0

EditorCamera()
app.run()
