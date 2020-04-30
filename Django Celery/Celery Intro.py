"""What is Celery

Celery is simple, flexible and reliable distributed system to process vast amount of messages, while providing
operations with the tools required to maintain such a system.

It's a task queue with focus on real time processing,while also supporting task scheduling.

What a task's Queue?

Task queues are used as a mechanism to distribute work across threads or machine.
A task queue's input is a unit of work is called task. Dedicated worker processes constantly monitor task queues
from new work to perform.

Celery communicate via messages, usually using a broker to mediate between clients and workers. To initiate
a task the clients adds a message to the queue, the broker then delivers the message to a worker.

A Celery system can consist of multiple workers anf brokers.

What do I need ?

Celery requires a message transport to send and receive messages.

Celery is easy to use and maintain, and it doesn't need configuration files.

Celery is a distributor task queue that allows you to send tasks to this queue that would be executed by celery outside
of the regular context of your app cd ..



"""