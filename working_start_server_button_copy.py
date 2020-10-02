from test_server_WSGI import start_app as start_server
import curio
import tkinter
import threading


class GUIAapp(object):
    def __init__(self):
        self.commands_queue = curio.UniversalQueue()
        self.event = curio.UniversalEvent()
        self.server_task = None
        self.server = start_server
        self.root = tkinter.Tk()
        self.root.geometry('820x600+300+100')
        self.root.resizable(False, False)
        self.button_on = tkinter.Button(self.root, text='Push me!', fg='green',
                                        command=lambda: self.commands_queue.put(self.button_on_click()))
        self.button_on.pack(expand=True, fill='x')
        # self.root.mainloop()

    async def button_on_click(self):
        print('button on clicked!')
        self.server_task = await self.start_server_app()
        server_id = await curio.current_task()
        print(self.server_task)
        # await server_proc.join()    # ??????????????????????????????????????
        curio.sleep(10)
        self.server_task.cancel()


    # async def server_work(self):
    #     print('Work start!')
    #     print('Work in process..')
    #     # server_result = await curio.spawn(curio.run_in_thread, start_server)
    #     server_result = await curio.run_in_thread(self.start_server_app)
    #     print('Work done!!!')

    async def start_server_app(self):
        print('Starting server....')
        start_server()
        print('fcuk')

    def loop_gui(self):
        threading.Thread(target=curio.run, args=(self.main_loop(),)).start()
        self.root.mainloop()

    async def main_loop(self):
        while True:
            command = await self.commands_queue.get()
            await command


if __name__ == '__main__':
    app = GUIAapp()
    app.loop_gui()
