import tempfile
import shutil
import subprocess as sp
import sys
import zipfile

from consts import TESTER_TOOL, PROJECT_PATH, LEVEL

from pathlib import Path


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
    tool_path = Path(n2t_path) / TESTER_TOOL
    setup_testing(tmp_path, submission_zip, Path(n2t_path))

    for tst_script_path in tmp_path.glob(f'{LEVEL * "*/"}*.tst'):
        if str(tst_script_path).endswith('VME.tst'):
            continue
        response = run_nand2tetris_test(str(tool_path), str(tst_script_path))
        if response is not None:
            print(tst_script_path.stem + ': ' + response)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        test_submission(*sys.argv[1:])
    else:
        print('Usage: {0} <nand2testris-dir-path> <zip-submission-file>'.format(sys.argv[0]))
