// import os
// import time
// from interruptingcow import timeout
// start_time = 0
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
// # this central processor is tailored to the modules we are expecting.
// # the modules to read:
//     # speed
//     # accuracy
//     # volume
//     # head gaze
//     # gestures

struct metric{
    std::string name;
    float max;
    float min;
    int allowance;
    int priority;
};

// # fuction: configure
// def configure(metrics):
std::vector<metric> configure(){
//     # this reads the configure file to set the thresholds for the metrics
//     outputDir = 'output/'
//     configFile = open(os.path.dirname(os.path.realpath(__file__))+'/config.txt', 'r')
//     for line in configFile:
    std::string line;
    std::ifstream configFile;
    configFile.open("central_proc/config.txt");
    if(configFile.is_open()){
        while(getline(configFile, line)){
//         configData = line.rstrip('\n').split()
            std::cout<<line;
        }
    }
    metric tmp = {"somthing", 2, 2, 2, 2};
    std::vector<metric> tmpV;
    tmpV.push_back(tmp);
    configFile.close();
    return tmpV;
}
//         m = configData[0]
//         metrics[m]["file"] = open(outputDir+m+".txt", 'r')
//         i = 1
//         while i < len(configData):
//             metrics[m][configData[i]] = float(configData[i+1])
//             print m+" "+configData[i]+" "+configData[i+1]
//             i += 2
//     configFile.close()

// # function: makeFeedbackDecision
// def makeFeedbackDecision(metrics, concerningData, feedbackFile):
//     # this function analyses concerningData to determine the best feedback to give
//     print "need to make a decision"
//     expireTime=10
//     currentPriority=100
//     currentFeedback=""
//     for m, info in concerningData.iteritems():
//         for i in info:
//             # expire old feedback - THIS COULD BE MORE SOPHISTICATED
//             if time.time()-i['timestamp'] > expireTime:
//                 info.remove(i)
//                 print "Removing a concern from "+m
//             # it compares the data to the allowance and priority given in config
//             # and finds the item that is the greatest outside the allowance and has the highest priority and flags this
//             print m+str(len(info))+" "+str(metrics[m]['priority'])
//             if len(info) > metrics[m]['allowance']:
//                 if metrics[m]['priority'] < currentPriority:
//                     currentFeedback=m+"_"+i['issue']
//                     currentPriority=metrics[m]['priority']
//     print currentFeedback
//     if currentFeedback != "":
//         # at the end, the flagged data is used to look up the correct response from the feedbackMap and writes to the file
//         feedbackMap = {
//             "head_gaze_low": 1,
//             "gestures_high": 2,
//             "posture_low": 3,
//             "accuracy_low": 4,
//             "speed_high": 5,
//             "volume_high": 7,
//             "speed_low": 6,
//             "volume_low": 8
//         }
//         feedbackFile.write(str(feedbackMap[currentFeedback])+"\n")

// # function: giveKineticFeedback
// def giveKineticFeedback(syncFile, metrics, historicalData, feedbackFile):
//     global start_time
//     # this function givesKineticFeedback based on the inputs
//     concerningData = {
//         "speed": [],
//         "accuracy": [],
//         "volume": [],
//         "head_gaze": []
//         # "gestures": []
//     }
//     stop = False
//     # while not told to stop:
//     print "giving feedback, time: "+str(time.time()-start_time)
//     while not stop:
//         concern = False
//         for m, info in metrics.iteritems():
//             # then reads in the latest data for all the files
//             f = info['file']
//             where = f.tell()
//             line = f.readline()
//             if not line or line in ['\n', '\r\n']:
//                 f.seek(where)
//                 continue
//             else:
//                 # saves this data for historical record
//                 data = line.rstrip('\n').split()
//                 historicalData[m].append(float(data[1]))
//                 print "reading "+m+" "+str(time.time()-float(data[0]))+" seconds after writing"
//                 # checks it against thresholds, adds to concerningData if a problem
//                 maybeAppend = {"timestamp": float(data[0]), "data": float(data[1])}
//                 if "min" in metrics[m]:
//                     if float(data[1]) < metrics[m]['min']:
//                         concern = True
//                         maybeAppend['issue'] = "low"
//                         concerningData[m].append(maybeAppend)
//                         print m+" concerningly low"
//                 if "max" in metrics[m]:
//                     if float(data[1]) > metrics[m]['max']:
//                         concern = True
//                         maybeAppend['issue'] = "high"
//                         concerningData[m].append(maybeAppend)
//                         print m+" concerningly high"
//         if concern:
//             makeFeedbackDecision(metrics, concerningData, feedbackFile)
//         # check if sync has said to stop
//         swhere = syncFile.tell()
//         sline = syncFile.readline()
//         if not line or line in ['\n', '\r\n']:
//             time.sleep(1)
//             syncFile.seek(where)
//         else:
//             if line.rstrip('\n') == "stop":
//                 stop = True

// # function: givePostFeedback
//     # this function aggregates the historical data
//     # then fills in string templates with the relevant data
//     # and writes these strings to file

int main(){
    std::vector<metric> metrics;
    metrics = configure();
    return 0;
}
// # function: main
// def main():
//     # this function is the main control
//     global start_time
//     metrics = {
//         "speed": {},
//         "accuracy": {},
//         "volume": {},
//         "head_gaze": {}
//         # "gestures": {}
//     }
//     historicalData = {
//         "speed": [],
//         "accuracy": [],
//         "volume": [],
//         "head_gaze": []
//         # "gestures": []
//     }

//     maxtime = 15 # in seconds
//     try: # do the following unless maxtime is reached:
//         with timeout(maxtime, exception=RuntimeError):
//             # it calls configure, passing in the metrics structure
//             configure(metrics)
//             start = False
//             syncFile = open('output/sync.txt', 'r')
//             feedbackFile = open('output/kinetic_feedback.txt', 'w')
//             while not start:
//                 # read sync
//                 where = syncFile.tell()
//                 line = syncFile.readline()
//                 if not line or line in ['\n', '\r\n']:
//                     time.sleep(1)
//                     syncFile.seek(where)
//                 else:
//                     if line.rstrip('\n') == "start":
//                         start = True
//             print "starting"
//             start_time = time.time()
//             giveKineticFeedback(syncFile, metrics, historicalData, feedbackFile)
//     except RuntimeError:
//         print "Stopping: run time exceeded "+str(maxtime)+" seconds"
//         pass

//     syncFile.close()
//     feedbackFile.close()
//     # givePostFeedback(historicalData)

// main()
