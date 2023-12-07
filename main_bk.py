import matplotlib.pyplot as plt
import neurokit2 as nk
import numpy as np
import pandas as pd
import pyscript as ps

def read_file_from_string(string: str):
    # Might need to change this depending on the file format
    # Remember it's coming from a string so newlines have already been replaced!
    return np.array(string[:-1].split(","), dtype=np.float32)

def do_one_thing():
	

# Handle data upload
def do_thing():
	size = 200000
    data = ps.Element("input_data")
    ecg = data.element.textContent
    #It will likely be too long for one bite
	#Try 200,000 numbers
	loops = len(ecg)//size
	for i in range(loops):
		last = i * size + size
		if last > len(ecg):
			last = len(ecg)
		chunk = do_one_thing(ecg[i*size:last])
	
    ecg = read_file_from_string(ecg)
    
    signals, rpeaks = nk.ecg_process(ecg, sampling_rate=128)
    ps.display("OK so far", target="mpl")
    df = pd.DataFrame(data={"peaks": rpeaks["ECG_R_Peaks"]})

    nk.ecg_plot(signals, rpeaks)

    plt.tight_layout()
    fig1 = plt.gcf()
    fig1.set_size_inches(10, 12, forward=True) 

    signals_html = ps.Element("signals")

    signals_html.element.innerText = df.to_string()

    ps.display(fig1, target="mpl")

    download_button = ps.Element("download_data")
    analyse_button = ps.Element("analyse_button")

    analyse_button.element.hidden = True
    download_button.element.hidden = False