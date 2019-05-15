from passporteye import read_mrz
import Filter


def mrz_tool(filename, except_score):  # Return 1 if image is success increase, 0 if failed, 2 if no need to change
    mrz_file = read_mrz(filename)
    method = 1
    count = 1
    while mrz_file == None or mrz_file.valid_score < except_score:
        if method == 1:  # First try to increase brightness
            path, new_frame = Filter.increase_brightness(filename, 3)  # return a path
            method = 2

        elif method == 2:  # Second try to increase contrast
            path, new_frame = Filter.increase_contrast(filename, 127)
            method = 3

        else:  # Last try to increase both
            path, new_frame = Filter.increase_brightness(path, 3)
            method = 4

        mrz_file = read_mrz(path) # Re-identify again

        if mrz_file == None:
            print(str(count) + ': ' + 'Failed')
            count += 1
            if method == 4:
                return filename, 0
            continue
        else:
            print(str(count) + ': ' + str(mrz_file.valid_score))
            count += 1

        if mrz_file.valid_score > except_score:
            return path, 1  # return a new frame


    if mrz_file.valid_score > except_score:
        return filename, 2


if __name__ == '__main__':
    filenames = ['images/passport_06.jpg', 'images/passport_07.jpg', 'images/passport_11.jpeg', 'images/passport_13.jpg']
    count = 1

    for filename in filenames:
        print('Test{}:'.format(count))
        path, variable = mrz_tool(filename, 80)
        if variable == 1:
            print('The new picture path is {}'.format(path))
        elif variable == 0:
            print('Picture filter is failed, return {}'.format(path))
        else:
            print('No need to change this picture, return {}'.format(path))
        count += 1
