"""Step 2 script: displays information about the runtime environment,
then computes a revenue figure with pandas."""
import platform
import socket

import pandas as pd

sales = pd.DataFrame({
    "product": ["keyboard", "mouse", "monitor", "headset"],
    "price": [49.90, 19.90, 189.00, 79.00],
    "quantity": [3, 5, 2, 4],
})
sales["total"] = sales["price"] * sales["quantity"]

print("Hello from a Docker container!")
print(f"Machine name: {socket.gethostname()}")
print(f"Python {platform.python_version()} | pandas {pd.__version__}")
print(f"Total revenue: {sales['total'].sum():.2f} EUR")
