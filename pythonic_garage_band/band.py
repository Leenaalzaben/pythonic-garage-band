# first Class
class Musician:
    """
    The musician performance.
    """

    instrument = ""
    solo = ""
    title = ""

    # Method 1
    def __init__(self, name):
        """
        Initializes a Musician instance.
        Args name : The name of the musician.
        """
        #  instance
        self.name = name

    # Method 2
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    # Meyhod 3
    def __repr__(self):
        return f"{self.title} instance. Name = {self.name}"

    # Method 4
    def get_instrument(self):
        return f"{self.instrument}"

    # Method 5
    def play_solo(self):
        return f"{self.solo}"


# 2nd Class
class Guitarist(Musician):
    """
    The guitarist performance.

    """

    instrument = "guitar"
    title = "Guitarist"
    solo = "face melting guitar solo"


# 3rd Class
class Bassist(Musician):
    """
    The Bassist performance.

    """

    instrument = "bass"
    title = "Bassist"
    solo = "bom bom buh bom"


# 4th Class
class Drummer(Musician):
    """
    The Drummer performance.

    """

    instrument = "drums"
    title = "Drummer"
    solo = "rattle boom crash"


# fifth Class
class Band:
    """
    Represents a band consisting of musicians.
    """

    # Method Band
    def __init__(self, name, members):
        """
        Initializes a Band instance.

        Args: The name of the band.
        And A list of Musician instances representing the band members.
        """
        #  instance
        self.name = name
        self.members = members
        Band.instances.append(self)

    # Method Band 2
    def play_solos(self):
        play_solos_list = []
        for member in self.members:
            play_solos_list.append(member.play_solo())
        return play_solos_list
    @classmethod
    # cls same of self

    def to_list(cls):
        
        """
        Return a list of all Band instances.
        """
        return cls.instances

    if __name__ == "__main__":
        print(Guitarist.instrument)
        print(Guitarist.title)
        print(Guitarist.solo)
        print(Bassist.instrument)
        print(Bassist.title)
        print(Bassist.solo)
        print(Drummer.instrument)
        print(Drummer.title)
        print(Drummer.solo)
        # print(f"My name is {cls.name} and I play {cls.instrument}")
