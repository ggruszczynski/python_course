from multiprocessing import Pool
import time

def f(x):
    # time.sleep(0.01)
    print (x*x)

if __name__ == '__main__':
    with Pool(processes=4) as pool:
    # pool = Pool(processes=10)
        pool.map(f, range(100))
        # r  = pool.map_async(f, range(10))
        # r = pool.map(f, range(10))
        # DO STUFF
        print('HERE')
        print('MORE')
        # r.wait()
        # pool.close()
        # pool.join()
        print('DONE')

    print('BYE')


raise FileExistsError