class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #reverse the positions of the cars and then go through them with a for loop
        new = sorted(zip(position, speed))

        container = []

        for position, speed in reversed(new):
            time = (target - position)/speed
            if container and time > container[-1]:
                container.append(time)
            elif not container:
                container.append(time)
        return len(container)


        