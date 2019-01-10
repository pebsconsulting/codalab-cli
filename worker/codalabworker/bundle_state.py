class RunResources(object):
    """
    Defines all the resource fields the server propagates to the worker for its runs
    """
    def __init__(self, cpus, gpus, docker_image, time, memory, disk, network):
        self.cpus = cpus  # type: int
        self.gpus = gpus  # type: int
        self.docker_image = docker_image  # type: str
        self.time = time  # type: int
        self.memory = memory  # type: int
        self.disk = disk  # type: int
        self.network = network  # type: bool

    @classmethod
    def from_dict(cls, dct):
        return cls(cpus=int(dct['cpus']),
                   gpus=int(dct['gpus']),
                   docker_image=dct['docker_image'],
                   time=int(dct['time']),
                   memory=int(dct['memory']),
                   disk=int(dct['disk']),
                   network=bool(dct['network']))


class WorkerRun(object):
    """
    Defines all the field the worker needs to check in with the server for its runs
    """
    def __init__(self, uuid, run_status, start_time, docker_image, info, state):
        self.uuid = uuid
        self.run_status = run_status
        self.start_time = start_time
        self.docker_image = docker_image
        self.info = info
        self.state = state


class State(object):
    """
    An enumeration of states that a bundle can be in.
    """

    # Waiting for contents to be uploaded
    UPLOADING = 'uploading'
    # Just created
    CREATED = 'created'
    # All the dependencies are met
    STAGED = 'staged'
    # Creating a make bundle.
    MAKING = 'making'
    # Waiting for the worker to start up.
    WAITING_FOR_WORKER_STARTUP = 'waiting_for_worker_startup'
    # Wait for the worker to start running the bundle.
    STARTING = 'starting'
    # Wait for worker to download dependencies and docker images
    PREPARING = 'preparing'
    # Actually running
    RUNNING = 'running'
    # Run finished and finalized server-side, tell worker to discard it
    FINALIZING = 'finalizing'
    # Done running and succeeded
    READY = 'ready'
    # Done running and failed
    FAILED = 'failed'
    # Killed by user
    KILLED = 'killed'
    # Assigned worker has gone offline
    WORKER_OFFLINE = 'worker_offline'

    OPTIONS = {
        CREATED,
        STAGED,
        MAKING,
        WAITING_FOR_WORKER_STARTUP,
        STARTING,
        RUNNING,
        READY,
        FAILED,
        PREPARING,
        FINALIZING,
    }
    ACTIVE_STATES = {MAKING, WAITING_FOR_WORKER_STARTUP, STARTING, RUNNING, FINALIZING, PREPARING}
    FINAL_STATES = {READY, FAILED, KILLED}
