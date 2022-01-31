from program import run
from solution import sol
from io import StringIO


class TestProgram():

    def solution_case(self, capsys, monkeypatch, *args):
        monkeypatch.setattr('sys.stdin', StringIO(f"{args[0]}\n" +
                                                  f"{args[1]}\n" +
                                                  f"{args[2]}\n"))
        sol()
        out, _ = capsys.readouterr()
        return out

    def test_case(self, capsys, monkeypatch, printer):
        consts = [
            (100.8, 20.5, 10.2),
            (20, 10, 5)
        ]
        for c in consts:
            printer(f"Try: {c}")
            monkeypatch.setattr('sys.stdin', StringIO(f"{c[0]}\n"+
                                                      f"{c[1]}\n"+
                                                      f"{c[2]}\n"))
            run()
            out, _ = capsys.readouterr()
            assert out == self.solution_case(capsys, monkeypatch, *c)