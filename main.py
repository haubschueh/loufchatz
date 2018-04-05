from communication.FreedomInterface import FreedomInterface

"""

"""

freedomBoard = FreedomInterface.getInstance()

freedomBoard.hello()
freedomBoard.goto_cube()
freedomBoard.lift_cube()
freedomBoard.drive()

# find the target

freedomBoard.stop()
freedomBoard.put_cube()
freedomBoard.drive()