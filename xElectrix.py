import json, os, sys
from imports import tools as T

def xElectrix(conf):
    T.printBanner(1, conf)
    T.shell(conf)
    T.printBanner(0, conf)

def main(prName):
    if(prName is not None):
        ProjectHQ = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        confFile = ProjectHQ+'/'+prName+'/xEProject.conf'
        if(os.path.exists(confFile)):
            with open(confFile, 'r') as Config:
                prConfig = json.loads(Config.read())
            
            xElectrix(prConfig)
        else:
            print("This Project does not use xElectrix!!")
            sys.exit(1)
    else:
        print("Feature Not Yet Supported!!")
        sys.exit(1)

if __name__ == "__main__" :
    main(prName=sys.argv[1] if len(sys.argv)>1 else None)