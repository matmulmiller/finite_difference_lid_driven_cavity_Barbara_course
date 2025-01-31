
def generate_batch(Re, mode):
    if mode == 'Train':
        batch = {'Re': Re, 'Sh': [0, 0.03125, 0.25, 0.375, 0.5], 'Sl': [0.03125, 0.25, 0.375, 0.4375, 0.5, 0.5625]}
    elif mode == 'Test':
        batch = {'Re': Re, 'Sh': [0, 0.015625, 0.3125, 0.625], 'Sl': [0.015625, 0.0625, 0.125, 0.3125, 0.75]}
        # batch = {'Re': Re, 'Sh': [0.625], 'Sl': [0.75]}
    elif mode == "Validation":
        batch = {'Re': Re, 'Sh': [0, 0.1875, 0.6875], 'Sl': [0.1875, 0.6875]}
    return batch
