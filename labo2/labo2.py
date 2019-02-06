import cozmo.robot
import KNN, SVM

if __name__ == '__main__':
    #cozmo.run_program(cozmo_program, use_3d_viewer=True, show_viewer_controls=True)
    cozmo.run_program(test_program, use_3d_viewer=True, show_viewer_controls=True)

def cozmo_program(robot: Robot):
	knn = KNN()
	knn.print_agent()
	return