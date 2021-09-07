from pathlib import Path
import tempfile
import shutil
import subprocess as sp
import sys
from xmldiff import main
import zipfile

from consts import PROJECT_PATH, LEVEL, USER_SCRIPT, USER_SCRIPT_LEVEL, USER_SCRIPT_REGEX


def compare_xmls(xml1, xml2):
    return len(main.diff_texts(xml1, xml2)) == 0


def run_user_script(test_dir: Path):
    for source in test_dir.glob(USER_SCRIPT_LEVEL * '*/' + USER_SCRIPT_REGEX):
        p = sp.Popen(['python3', str(test_dir / USER_SCRIPT), str(source)], stderr=sp.PIPE)
        if 0 == p.wait():
            return None
        return p.stderr.read().decode().strip()


def run_nand2tetris_test(tool_path: str, tst_path: str):
    p = sp.Popen([tool_path, tst_path], stderr=sp.PIPE)
    if 0 == p.wait():
        return None
    return p.stderr.read().decode().strip()


def setup_testing(testing_dir: Path, submission_zip: str, n2t_path: Path):
    for f in (n2t_path / PROJECT_PATH).glob('*'):
        shutil.copy(str(f), str(testing_dir / f.name))
    with zipfile.ZipFile(submission_zip, 'r') as zip_ref:
        zip_ref.extractall(testing_dir)


def test_submission(n2t_path: str, submission_zip: str):
    tmp_path = Path(tempfile.mkdtemp())
    setup_testing(tmp_path, submission_zip, Path(n2t_path))

    run_user_script(tmp_path)

    for xml_path in tmp_path.glob(f'{LEVEL * "*/"}*.xml'):
        if not compare_xmls(xml_path, Path(n2t_path) / PROJECT_PATH / xml_path.relative_to(tmp_path)):
            print('XML of ' + xml_path.stem + ' is different from the compared one.')


if __name__ == '__main__':
    if len(sys.argv) == 3:
        test_submission(*sys.argv[1:])
    else:
        print('Usage: {0} <nand2testris-dir-path> <zip-submission-file>'.format(sys.argv[0]))
