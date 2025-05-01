import pytest
from pathlib import Path
import shutil
import tempfile
from check_blog_titles import PASS, FAIL, check_blog_titles


@pytest.fixture
def test_dir():
    temp_dir = Path(tempfile.mkdtemp())
    yield temp_dir
    shutil.rmtree(temp_dir)


def create_test_blog(base_dir: Path, folder_name: str, title: str) -> Path:
    blog_dir = base_dir / folder_name
    blog_dir.mkdir(parents=True)
    with open(blog_dir / "contents.lr", "w") as f:
        f.write(f"title: {title}\n")
    return blog_dir


def test_matching_folder_name(test_dir):
    create_test_blog(test_dir, "my-first-post", "My First Post")
    result = check_blog_titles(test_dir)
    assert result == PASS


def test_mismatched_folder_name(test_dir):
    create_test_blog(test_dir, "wrong-name", "My First Post")
    result = check_blog_titles(test_dir)
    assert result == FAIL


def test_fix_folder_name(test_dir):
    original_dir = create_test_blog(test_dir, "wrong-name", "My First Post")
    result = check_blog_titles(test_dir, fix=True)
    assert result == PASS
    assert not original_dir.exists()
    assert (test_dir / "my-first-post").exists()
