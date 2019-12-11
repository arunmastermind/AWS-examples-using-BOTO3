import mxnet as mx
from mxnet.gluon.model_zoo import vision
squeezenet = vision.squeezenet_v1(pretrained=True, ctx=mx.cpu())

# To export, you need to hybridize your gluon model,
squeezenet.hybridize()

# SqueezeNet’s input pattern is 224 pixel X 224 pixel images. Prepare a fake image,
fake_image = mx.nd.random.uniform(shape=(1,3,224,224), ctx=mx.cpu())

# Run the model once.
result = squeezenet(fake_image)

# Now you can export the model. You can use a path if you want ‘models/squeezenet’.
squeezenet.export(‘squeezenet')