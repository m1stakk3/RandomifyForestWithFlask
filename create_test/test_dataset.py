from logger import logging
import os
import pandas as pd
import random


save_path: str = os.path.abspath("./create_test/test_dataset.csv")


def create_test_dataset() -> None:
    logging.info("Creating 1000 rows test dataset")
    df = pd.DataFrame(
        [
            {
                "id": _,
                "battery_power": random.randint(600, 2000),
                "blue": random.choice([0, 1]),
                "clock_speed": round(random.uniform(0, 2), 1),
                "dual_sim": random.choice([0, 1]),
                "fc": random.randint(5, 20),
                "four_g": random.choice([0, 1]),
                "int_memory": random.randint(20, 70),
                "m_dep": round(random.uniform(0, 5), 1),
                "mobile_wt": random.randint(100, 300),
                "n_cores": random.randint(1, 5),
                "pc": random.randint(1, 5),
                "px_height": random.randint(100, 2000),
                "px_width": random.randint(1000, 4000),
                "ram": random.randint(2000, 4000),
                "sc_h": random.randint(1, 10),
                "sc_w": random.randint(1, 10),
                "talk_time": random.randint(5, 20),
                "three_g": random.choice([0, 1]),
                "touch_screen": random.choice([0, 1]),
                "wifi": random.choice([0, 1])
            }
            for _ in range(1, 1001)
        ]
    )

    df.to_csv(save_path, index=False)
    if not os.path.exists(save_path):
        logging.error("Dataset was not created!")
        raise FileNotFoundError("Датасет не был создан!")
    logging.info("Dataset created. Path = %s", save_path)
