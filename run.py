"""
The entry point for the harvester
"""

from StreamHarvester import StreamHarvester

if __name__ == '__main__':
    SH = StreamHarvester(0)
    SH.harvest()
