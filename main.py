def main(): #Program runs through this function, and allawos selection of funtion to use
    results = readFile('marathon.txt')
    option = ''
    while option != 'Q':
        menu()
        option = input('Select option: ')
        if option == 'S':
            displayCompetitor(results)
        elif option == 'I':
            displayNbrInInterval(results)
          
def readFile(filename): #Reads the file, assigns info from the file to a dictionary, then adds the dictionary to a list
  readFile = open(filename)
  results = []
  for eachLine in readFile:
    RunnerInfo = {'id':'','time':'','firstname':'','lastname':''}
    SplitLine = eachLine.split(',')
    RunnerInfo['id'] = SplitLine[0]
    RunnerInfo['time'] = SplitLine[1]
    RunnerInfo['firstname'] = SplitLine[2]
    RunnerInfo['lastname'] = SplitLine[3]
    results.append(RunnerInfo)
  return results

def getIntervalData(shortest, longest, results):#Two paramenters that decides what goes into the mean and count, "result" is a datasheet from funtion "main",returns in dictonary
  CountMean = {'count':0,'mean':0}
  MeanCalc = 0
  for i in range(len(results)):
    MeanCalcInt = getSecs(results[i]['time'])
    if MeanCalcInt >= shortest and MeanCalcInt <= longest:
      MeanCalc += MeanCalcInt
      CountMean['count'] += 1
  CountMean['mean'] = MeanCalc / CountMean['count']
  return CountMean

def displayCompetitor(results): #Checks list "results" to see if it find ID and then prints out info assigned to ID   
    idNo = input('Enter competitor ID:')
    found = False
    for competitor in results:
        if competitor['id'] == idNo:
            displayCompetitorInfo(competitor)
            found = True
    if not found:
        print('Competitor not found')
    
def displayCompetitorInfo(competitor): #prints out "id" if "id" can be found in "results" in the function "displayCompetitor"
    print('ID :',competitor['id'])
    print('First Name :', competitor['firstname'])
    print('First Name :', competitor['lastname'])

def displayNbrInInterval(results):#Prints out information about set intervals
    startTime = input('Enter start time of interval (hh:mm:ss): ')
    startSecs = getSecs(startTime)
    endTime = input('Enter end time of interval (hh:mm:ss): ')
    endSecs = getSecs(endTime)
    intervalData = getIntervalData(startSecs, endSecs, results)
    print('Number of competitors finishing in this interval = ', intervalData['count'])
    if intervalData['count'] != 0:
        secs = intervalData['mean']
        mins = secs//60
        secs = secs%60
        hours = mins//60
        mins = mins%60
        print('Mean time in interval is ',int(hours),'hours',int(mins),'minutes','and ',int(secs),'seconds')
    else:
        print('No competitors in interval')

def getSecs(time): #Converts a string resembling time in the format hh:mm:ss to int representing seconds
    timeSplit = time.split(':')
    seconds = int(timeSplit[2]) + 60*int(timeSplit[1]) + 60*60*int(timeSplit[0])
    return seconds
                      
def menu(): #Menu that alows you to read what you can choose in function "main"
    print('Options are:')
    print('S - Show data for a competitor')
    print('I - Show statistics for competitors finishing in a given interval')
    print('Q - Quit the program')

if __name__ == "__main__":
  main()
