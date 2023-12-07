import matplotlib.pyplot as plt
import neurokit2 as nk
import numpy as np
import pandas as pd
import pyscript as ps

def read_file_from_string(string: str):
    # Might need to change this depending on the file format
    # Remember it's coming from a string so newlines have already been replaced!
    return np.array(string[:-1], dtype=np.float32)

def do_one_thing(ecg_bit,run):
	ecg_bit = read_file_from_string(ecg_bit)
	
	signals, rpeaks = nk.ecg_process(ecg_bit, sampling_rate=128)
	if run==0:
		nk.ecg_plot(signals, rpeaks)
		plt.tight_layout()
		fig1 = plt.gcf()
		fig1.set_size_inches(10, 12, forward=True) 
		ps.display(fig1, target="mpl")
	df = pd.DataFrame(data={"peaks": rpeaks["ECG_R_Peaks"]})
	return df
	

# Handle data upload
def do_thing():
	size = 100000
	masterdf = pd.DataFrame(data={"peaks": [0]})
	data = ps.Element("input_data")
	ecg = data.element.textContent.split(",")
	ps.display(f"ecg length {len(ecg)}", target="mpl")
	#It will likely be too long for one bite
	#Try "size" numbers
	loops = len(ecg)//size
	for i in range(loops):
		last = i * size + size
		if last > len(ecg):
			last = len(ecg)
		chunk = do_one_thing(ecg[i*size:last],i)
		masterdf=pd.concat([masterdf,chunk+max(masterdf["peaks"])])
		
	signals_html = ps.Element("signals")
	signals_html.element.innerText = masterdf.diff()[1:].to_string()
	#signals_html.element.innerText = masterdf.diff()[1:].values
	
	download_button = ps.Element("download_data")
	analyse_button = ps.Element("analyse_button")
	analyse_button.element.hidden = True
	download_button.element.hidden = False