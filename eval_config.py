from util import mkdir


# directory to store the results
results_dir = './results/'
mkdir(results_dir)

# root to the testsets
# dataroot = './dataset/test/'
dataroot = '../../../../scratch/kkaterga/GenImage'

# list of synthesis algorithms
vals = ['DALLE3', 'Firefly', 'Gemini']

# indicates if corresponding testset has multiple classes
multiclass = [0, 0, 0]

# model
model_path = 'weights/blur_jpg_prob0.5.pth'
