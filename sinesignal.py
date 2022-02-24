import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
time_range = np.arange(0, 5, 0.001)

sine_wave = (1 * np.sin((2 * np.pi * 2 * time_range / 5) + ((np.pi / 180) * 120))) + (5 * np.sin((2 * np.pi * 5 * time_range / 5) + ((np.pi / 180) * 10))) + (10 * np.sin((2 * np.pi * 13 * time_range / 5) + ((np.pi / 180) * 13))) + (5 * np.sin((2 * np.pi * 6 * time_range / 5) + ((np.pi / 180) * 50)))
df = pd.DataFrame({"Time" : time_range, "Amplitude" : sine_wave})
df.to_csv("ComplexSignal.csv", index=False)

plt.plot(time_range, sine_wave)
plt.show()