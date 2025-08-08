
class Television:
    """
    Class to mimic a functioning tv
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):

        self.status: bool = False
        self.muted: bool = False
        self.volume: int = self.MIN_VOLUME
        self.channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles power variable for tv
        """
        
        if not self.status:
            self.status = True

        else:
            self.status = False

    def mute(self) -> None:
        """
        Toggles mute status for tv
        """

        if self.status:

            if not self.muted:
                self.muted = True

            else:
                self.muted = False

    def channel_up(self) -> None:
        """
        Increments the tv's channel up and goes back to the min channel if over the max
        """

        if self.status:

            if self.channel < self.MAX_CHANNEL:
                self.channel += 1

            else:
                self.channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Increments the tv's channel down and goes back to the max channel if under the min
        """

        if self.status:

            if self.channel > self.MIN_CHANNEL:
                self.channel -= 1

            else:
                self.channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increments volume up, toggles mute off if on, does not increment further if at volume max
        """

        if self.status:
            
            if self.muted:
                self.muted = False

            if self.volume < self.MAX_VOLUME:
                self.volume += 1

    def volume_down(self) -> None:
        """
        Increments the volume down,toggles mute off, does not increment further if at min volume
        """

        if self.status:

            if self.muted:
                self.muted = False

            if self.volume > self.MIN_VOLUME:
                self.volume -= 1

    def __str__(self) -> str:
        """
        Get Televisions' Power, Channel, and volume
        :return: fstring of power channel and volume
        """

        if self.muted:
            return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.MIN_VOLUME}'
        
        else:
            return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'
