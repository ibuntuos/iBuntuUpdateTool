import os

def Convert(string): 
    li = list(string.split(" ")) 
    return li 

def packagelist():
	systeminstalled= os.popen("gzip -dc /var/log/installer/initial-status.gz | sed -n 's/^Package: //p' | sort -u").read()
	systeminstalled=systeminstalled.replace('\n', ' ')
	manualinstalled= os.popen("apt-mark showmanual").read()
	manualinstalled=manualinstalled.replace('\n', ' ')
	final=[]

  
	systeminstalled=(Convert(systeminstalled)) 
	manualinstalled=(Convert(manualinstalled)) 


	for i in manualinstalled:
		if i not in systeminstalled:
			final.append(i)


	return(final)
