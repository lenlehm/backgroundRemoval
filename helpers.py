import matplotlib.pyplot as plt

def visualize_img(img, description_string="", x_label="", y_label=""):
    plt.figure()
    plt.title(description_string)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.gray()
    plt.imshow(img)
    plt.show()