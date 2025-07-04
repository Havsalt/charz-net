from __future__ import annotations
# TODO: Implement `Server` mixin class for `charz_core.Engine`

from socket import socket as Socket
from typing import Any

from charz_core import Self

from ._socket_setup import SocketSetup
from ._annotations import Host, Port


class Server:  # Component (mixin class)
    socket_setup: SocketSetup
    backlog: int | None = None
    _socket: Socket  # Read-only

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        instance = super().__new__(cls, *args, **kwargs)
        instance._socket = Socket(
            instance.socket_setup.address_family,
            instance.socket_setup.socket_kind,
        )
        instance.socket.bind(instance.address)
        if instance.backlog is None:
            instance.socket.listen()  # Uses default backlog
        else:
            instance.socket.listen(instance.backlog)
        # TODO: Start new thread that listens
        return instance

    @property
    def socket(self) -> Socket:
        return self._socket

    @property
    def address(self) -> tuple[Host, Port]:
        return (self.socket_setup.host, self.socket_setup.port)
