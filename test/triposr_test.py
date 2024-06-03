import os.path
import subprocess
import unittest
from os import listdir
from os.path import isfile, join, dirname, abspath
from PIL import Image
from PIL import ImageChops


class MyTestCase(unittest.TestCase):

    def before_test(self):
        cur_dir: str = dirname(os.path.abspath(__file__))
        path_to_examples: str = "examples"
        if cur_dir != "":
            path_to_examples = cur_dir + "/" + path_to_examples
        examples_file_names: list[str] = [path_to_examples + "/" + f for f in listdir(path=path_to_examples)
                                          if isfile(join(path_to_examples, f))]
        run_command: str = "python3 " + dirname(cur_dir) + "/run.py " \
                           + " ".join(examples_file_names) \
                           + " --output-dir " + cur_dir + "/actual"
        print(run_command)
        process = subprocess.run(run_command, shell=True)
        self.return_code = process.returncode
        path_to_expected: str = "expected"
        if cur_dir != "":
            path_to_expected = cur_dir + "/" + path_to_expected
        self.expected_image_filename_paths: list[str] = [path_to_expected + "/" + str(i) + "/input.png"
                                                         for i in range(0, len(listdir(path=path_to_expected)))]
        self.expected_obj_filename_paths: list[str] = [path_to_expected + "/" + str(i) + "/mesh.obj"
                                                       for i in range(0, len(listdir(path=path_to_expected)))]
        self.actual_image_filename_paths: list[str] = []
        self.actual_obj_filename_paths: list[str] = []
        if self.return_code == 0:
            path_to_actual: str = "actual"
            if cur_dir != "":
                path_to_actual = cur_dir + "/" + path_to_actual
            self.actual_image_filename_paths = [path_to_actual + "/" + str(i) + "/input.png"
                                                for i in range(0, len(listdir(path=path_to_actual)))]
            self.actual_obj_filename_paths = [path_to_actual + "/" + str(i) + "/mesh.obj"
                                              for i in range(0, len(listdir(path=path_to_actual)))]

    def test_triposr(self):
        self.before_test()
        self.assertEqual(self.return_code, 0, "Program failed with test data")

        self.assertNotEqual(len(self.actual_image_filename_paths), 0, "No formatted image founded")
        self.assertEqual(len(self.expected_image_filename_paths), len(self.actual_image_filename_paths),
                         "Expected images count != Actual images count")
        for i in range(len(self.expected_image_filename_paths)):
            expected_image: Image = Image.open(self.expected_image_filename_paths[i])
            actual_image: Image = Image.open(self.actual_image_filename_paths[i])
            diff = ImageChops.difference(expected_image, actual_image)
            self.assertEqual(diff.getbbox(), None, f"Expected \\ Actual Image_{i} are different")

        self.assertNotEqual(len(self.actual_obj_filename_paths), 0, "No test .obj founded")
        self.assertEqual(len(self.expected_obj_filename_paths), len(self.actual_obj_filename_paths),
                         "Expected objects count != Actual objects count")
        for i in range(len(self.expected_obj_filename_paths)):
            expected_file_size: int = os.path.getsize(self.expected_obj_filename_paths[i])
            actual_file_size: int = os.path.getsize(self.actual_obj_filename_paths[i])
            self.assertAlmostEqual(expected_file_size, actual_file_size, delta=expected_file_size)


if __name__ == '__main__':
    unittest.main()
