from multiprocessing import Pool

def theTask(dataObj):  
    # Do some randon shit on the dataObj and return a result
    res=int(dataObj['index']) # Write out the shit into theTask
    return res

if __name__ == '__main__':

    # Define the dataset: Array of objects
    dataset = [{'index':str(x), 'data' : "data item {0}".format(x)} for x in range(1,10000)]

    # Output the dataset
    print ('Dataset size: ' + str(len(dataset)))

    # Run this with a pool of 5 agents having a chunksize of 3 until finished
    agents = 4
    chunksize = 100
    with Pool(processes=agents) as pool:
        result = pool.map(theTask, dataset, chunksize)

    # Output the result
    print ('Result:  ' + str(result))
