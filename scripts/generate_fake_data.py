from forest_inventory.forests.factories import ForestFactory

def run():
    print("Creating inital data")
    ForestFactory.create_batch(size=50)
    # create a specific one for search tests
    ForestFactory.create(name="My Forest")
    print("Inital data done")

