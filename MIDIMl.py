import tensorflow as tf
import tensorflow_io as tfio

# audio = tfio.audio.AudioIOTensor('gs://cloud-samples-tests/speech/brooklyn.flac')

import tensorflow as tf

dataset = tf.keras.utils.audio_dataset_from_directory(
    "path/to/audio/directory",
    batch_size=32,
    labels='inferred'  # Infers labels from subdirectory names
)
