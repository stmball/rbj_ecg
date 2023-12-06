import matplotlib.pyplot as plt
import neurokit2 as nk
import numpy as np
import pandas as pd
import pyscript as ps

def read_file_from_string(string: str, loop: int):
    # Might need to change this depending on the file format
    # Remember it's coming from a string so newlines have already been replaced!
	# Throw away the first 20 rows in the first chunk due to headers!
	if loop == 0:
		return np.array(string[20:-1], dtype=np.float32)
	else:
		return np.array(string[:-1], dtype=np.float32)

def do_one_thing(ecg_bit, loop, SI, species):
	ecg_bit = read_file_from_string(ecg_bit, loop)
	factor = 1.0
	if species.lower() == "rat":
		factor = 7.0
	elif species.lower() == "mouse":
		factor = 8.0
	elif species.lower() == "rabbit":
		factor = 3.0
	try: 	
		signals, rpeaks = nk.ecg_process(ecg_bit, sampling_rate=int(SI/factor))
		rpeaks["sampling_rate"] = SI
		signals["ECG_Rate"]=signals["ECG_Rate"]*factor
		if loop==0:
			nk.ecg_plot(signals, rpeaks)
			plt.tight_layout()
			fig1 = plt.gcf()
			fig1.set_size_inches(15, 10, forward=True) 
			ps.display(fig1, target="mpl")
		df = pd.DataFrame(data={"peaks": rpeaks["ECG_R_Peaks"]})
	except:
		df = pd.DataFrame(data={"peaks": [0]})
	return df
	

# Handle data upload
def do_thing():
	#Get the button handles ready for use
	processing = ps.Element("processing")
	download_button = ps.Element("download_data")
	analyse_button = ps.Element("analyse_button")
	upload_button = ps.Element("upload_button")
	analyse_button.element.hidden = True
	processing.element.hidden = False

	size = 10000
	masterdf = pd.DataFrame(data={"peaks": [0]})

	data = ps.Element("filename")
	filename = data.value	
	
	data = ps.Element("input_data")
	ecg = data.element.textContent.split(",")
	
	data = ps.Element("Species")
	species =  data.value
	
	data = ps.Element("Sample_Interval")
	si = int(data.value)
	
	ps.display(filename, target="mpl" )
	ps.display(f"ecg length {len(ecg)}", target="mpl")
	ps.display(f"species {species}", target="mpl")
	ps.display(f"Sample Interval {si}", target="mpl")
	
	#It will likely be too long for one bite
	#Try "size" numbers
	loops = len(ecg)//size
	for i in range(loops):
		last = i * size + size
		if last > len(ecg):
			last = len(ecg)
		chunk = do_one_thing(ecg[i*size:last],i, si, species)
		masterdf=pd.concat([masterdf,chunk+max(masterdf["peaks"])])
		
	signals_html = ps.Element("signals")
	signals_html.element.innerText = masterdf.diff()[1:].to_string()
	#signals_html.element.innerText = masterdf.diff()[1:].values
	

	analyse_button.element.hidden = True
	download_button.element.hidden = False
	upload_button.element.hidden = False
	processing.element.hidden = True