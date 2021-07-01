import multiprocessing
lock=multiprocessing.RLock()                    #递归锁
# lock=multiprocessing.Lock()                   #同步锁
# lock=multiprocessing.Event()                  #锁全部，释放全部
# lock=multiprocessing.Condition()              #条件锁
# lock=multiprocessing.BoundedSemaphore(n)      #一次锁n个
def test(arg):
    print('进程锁')
    lock.acquire()
    time.sleep(2)
    print(arg)
    lock.release()

if __name__ == '__main__':
    p=multiprocessing.Process(target=test,args=(1,))
    p.start()

    d=multiprocessing.Process(target=test,args=(2,))
    d.start()