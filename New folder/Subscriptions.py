# -*- mode: python; python-indent: 4 -*-
import ncs
from ncs.application import Service
from ncs.dp import Action
import ncs.cdb as cdb
import ncs.maapi as maapi
from ncs_pyvm import NcsPyVM


import _namespaces.test_ns as ns

import socket
import threading

_schemas_loaded = False


# ---------------
# ACTIONS EXAMPLE
# ---------------
# class DoubleAction(Action):
#     @Action.action
#     def cb_action(self, uinfo, name, kp, input, output, trans):
#         self.log.info('action name: ', name)
#         self.log.info('action input.number: ', input.number)
# 
#         # Updating the output data structure will result in a response
#         # being returned to the caller.
#         output.result = input.number * 2

class Subcriber(Action):
    @Action.action
    def __init__(self,prio,path,debug,input,output,name):
        self.log.info('action name: ',name)
        self.log.info('input: ', input)
        m = maapi.Maapi()
        self.sock = socket.socket()
        self.prio = prio 
        self.path = path
        self.debug = debug
        global _schemas_loaded
        
        if _schemas_loaded is False:
            ms = socket.socket()
            maapi.connect(sock=ms,ip='127.0.0.1',port=_ncs.NCS_PORT)
            maapi.load_schemas(ms)
            ms.close()
         
         
        cdb.connect(self.sock, type=cdb.DATA_SOCKET, ip='127.0.0.1',
                    port=_ncs.NCS_PORT, path=self.path)
        self.subid = cdb.subscribe(self.sock, prio=self.prio, path=self.path,
                                   nspace=ns.ns.hash)
        cdb.subscribe_done(self.sock)
        self.debug("Subscription {0}, subscribed to {1}".format(self.subid,
                                                                self.path))

    def wait(self):
        cdb.read_subscription_socket(self.sock)

    def ack(self):
        cdb.sync_subscription_socket(self.sock, cdb.DONE_PRIORITY)

    def diff_iter(self):
        def iterator(kp, op, oldv, newv, state):
            self.debug(
                "diffIterate: kp= {0}, OP= {1}, old_value={2}, new_value={3}"
                .format(str(kp), op, str(oldv), str(newv)))
            return _ncs.ITER_RECURSE
        cdb.diff_iterate(self.sock, self.subid, iterator, 0, None)
    
    def diff_iter_loop(self):
        while True:
            self.wait()
            self.diff_iter()
            self.ack()

    def close(self):
        cdb.end_session(self.sock)
        cdb.close(self.sock)
        
        
class Plaincdbsub(Action):
    def __init__(self, *args, **kwds):
        # Setup the NCS object, containing mechanisms
        # for communicating between NCS and this User code.
        self._ncs = NcsPyVM(*args, **kwds)
        self.debug('--- Service INIT OBJECT')
        # Register our 'finish' callback
        self._finish_cb = lambda: self.finish()

        self.sub = Subscriber(prio=100, path="/devices/device{ex0}/config",
                              debug=self.debug)

        self._ncs.reg_finish(self._finish_cb)

        self._stopevent = threading.Event()

    # This method is supposed to start the User application
    def run(self):
        self.debug('Running diff iter loop')
        self.sub.diff_iter_loop()

    # Just a convenient logging function
    def debug(self, line):
        self._ncs.debug(line)

    # Callback that will be invoked by NCS when the system is shutdown.
    # Make sure to shutdown the User code, including any User created threads.
    def finish(self):
        self.debug(' PlainSub in finish () =>\n')
        self.sub.close()
        self._stopevent.set()
        self.debug(' PlainSub in finish () => ok\n')               
# # ------------------------
# # SERVICE CALLBACK EXAMPLE
# # ------------------------
# class ServiceCallbacks(Service):
# 
#     # The create() callback is invoked inside NCS FASTMAP and
#     # must always exist.
#     @Service.create
#     def cb_create(self, tctx, root, service, proplist):
#         self.log.info('Service create(service=', service._path, ')')
# 
# 
#     # The pre_modification() and post_modification() callbacks are optional,
#     # and are invoked outside FASTMAP. pre_modification() is invoked before
#     # create, update, or delete of the service, as indicated by the enum
#     # ncs_service_operation op parameter. Conversely
#     # post_modification() is invoked after create, update, or delete
#     # of the service. These functions can be useful e.g. for
#     # allocations that should be stored and existing also when the
#     # service instance is removed.
# 
#     # @Service.pre_lock_create
#     # def cb_pre_lock_create(self, tctx, root, service, proplist):
#     #     self.log.info('Service plcreate(service=', service._path, ')')
# 
#     # @Service.pre_modification
#     # def cb_pre_modification(self, tctx, op, kp, root, proplist):
#     #     self.log.info('Service premod(service=', kp, ')')
# 
#     # @Service.post_modification
#     # def cb_post_modification(self, tctx, op, kp, root, proplist):
#     #     self.log.info('Service premod(service=', kp, ')')


# ---------------------------------------------
# COMPONENT THREAD THAT WILL BE STARTED BY NCS.
# ---------------------------------------------
class Main(ncs.application.Application):
    def setup(self):
        # The application class sets up logging for us. It is accessible
        # through 'self.log' and is a ncs.log.Log instance.
        self.log.info('Main RUNNING')

        # Service callbacks require a registration for a 'service point',
        # as specified in the corresponding data model.
        #

        # When using actions, this is how we register them:
        #
        self.register_action('subscriptions-community-action', SetSubscription)

        # If we registered any callback(s) above, the Application class
        # took care of creating a daemon (related to the service/action point).

        # When this setup method is finished, all registrations are
        # considered done and the application is 'started'.

    def teardown(self):
        # When the application is finished (which would happen if NCS went
        # down, packages were reloaded or some error occurred) this teardown
        # method will be called.

        self.log.info('Main FINISHED')
