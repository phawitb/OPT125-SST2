SEED = 42
BATCH_SIZE = 32        # ค่า default สำหรับวิธีอื่น

# --- Networking / Fed settings ---
SERVER_IP   = "192.168.1.45"   # เปลี่ยนให้ตรงกับเครื่อง Server
SERVER_PORT = 50053
NUM_CLIENTS = 2
ROUNDS      = 5                 # จำนวนรอบ FedAvg

BACKPROP = {
    "MAX_STEPS":    100,
    "EVAL_EVERY":   10,
    "LOG_EVERY":    2,
    "SAVE_EVERY":   5,
    "GRAD_ACCUM":   1,
    "WARMUP_STEPS": 10,
    "LEARNING_RATE": 5e-5,
    "WEIGHT_DECAY": 0.0,
    "BATCH_SIZE":   8,
    "SEED":         42,

    "LOCAL_STEPS":   50,   # จำนวน step ที่ client train ต่อรอบ
    "ROUNDS":      20
}

# ------- Zeroth-Order (ZO-SGD) -------

# ZO = {
#     "MAX_STEPS":     10000,
#     "EVAL_EVERY":    100,
#     "LOG_EVERY":     20,
#     "SAVE_EVERY":    100,
#     "GRAD_ACCUM":    4,        # รวม 4 batches ก่อนอัปเดต
#     "MU":            1e-3,
#     "P":             5,       # หรือ 5 แต่ใช้ orthogonal
#     "LEARNING_RATE": 5e-6,
#     "WEIGHT_DECAY":  0.0,
#     "BATCH_SIZE":    8,
#     "SEED":          42,
# }

ZO = {
    "MAX_STEPS":     100,
    "LOCAL_STEPS":   10,       # ZO steps per round
    "EVAL_EVERY":    5,
    "LOG_EVERY":     1,
    "SAVE_EVERY":    10,
    "GRAD_ACCUM":    1,
    "MU":            1e-3,
    "P":             5,
    "LEARNING_RATE": 1e-4,
    "WEIGHT_DECAY":  0.0,
    "BATCH_SIZE":    4,
    "SEED":          42,
}


