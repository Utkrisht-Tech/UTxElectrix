def printBanner(flg, det):
    if(flg):
        banner=["| UTxElectrix is Now Managing {} v{} [{}] |".format(det["name"],det["version"],det["stage"]),"[Enter help or ? to display list of Commands]"]
        l=len(banner[0])
        print("\n{:5s}{}\n{:5s}{}\n{:5s}{}\n\n{:5s}{}".format('',"#"*l,'',banner[0],'',"#"*l,'',banner[1]))
    else:
        print("\n{:8s}{}".format('',"| Thank You Chief |"))
        exit(1)

availCmds = {
	"help": {"desc": "Displays this help-text", "arg": 0},
	"?": {"desc": "Displays this help-text", "arg": 0},
	"show": {
		"project": {
			"details": {"desc": "Prints general details for current project.", "arg": 100},
			"stats": {"desc": "Prints detailed stats for current project.", "arg": 101}
		},
        "build-stats": {"desc": "Prints stats for current project's builds.", "arg": 10},
        "test-stats": {"desc": "Prints stats for current project's tests.", "arg": 11}
    },
	"start": {
		"build": {"desc": "Starts the build according to details in `.conf` files.", "arg": 20},
		"tests": {"desc": "Starts and asserts tests prepared in `.testx` files.", "arg": 21}
	},
    "remove": {
        "builds": {"desc": "Removes all files associated with the range of [Valid_Build_No.'s] or all builds for current project.*See Docs*", "arg": 30}
    },
	"quit": {"desc": "Exit xElectrix Shell", "arg": -1},
	"q": {"desc": "Exit xElectrix Shell", "arg": -1}
}

def showHelp():
	STR="\n{:8s}{:24s} - {}\n{:8s}{:24s} - {}\n{:8s}{:8s}{:8s}{:8s} - {}\n{:24s}{:8s} - {}\n{:8s}{:8s}{:16s} - {}\n{:16s}{:16s} - {}\n{:8s}{:24s} - {}\n{:8s}{:24s} - {}"
	print(STR)

def cmdParser(rc,tmp):
	if(rc==0):
		showHelp()
	else:
		return -1
	return tmp

def shell(tmp):
    flg=None
    while(flg==None):
        cmd=input("\n{:5s}{}".format('',"Enter Command: ")).split()
        toCheck=availCmds
        for x in cmd:
            x=x.strip()
            if(x in toCheck.keys()):
                if("arg" in toCheck[x].keys()):
                    flg=toCheck[x]["arg"]
                    break
                else:
                    toCheck=toCheck[x]
            else:
				print("{:20s}{}".format('',"!! Invalid Command !!"))
				break
	tmp=cmdParser(flg,tmp)
	if(tmp!=-1):
		shell(tmp)
	else:
		return
