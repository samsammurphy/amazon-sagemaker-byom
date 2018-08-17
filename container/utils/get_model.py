"""
This will download the ResNet50 model with weights.

It represents your lovingly crafter model that you would
like to deploy to the cloud using a docker container
"""

def download_ResNet50():

    import os
    os.makedirs('./model', exist_ok=True)

    from keras.applications import ResNet50
    model = ResNet50(weights='imagenet')

    # serialize model to JSON
    model_json = model.to_json()
    with open('./model/model.json', 'w') as json_file:
        json_file.write(model_json)

    # serialize weights to HDF5
    model.save_weights('./model/weights.hdf5')