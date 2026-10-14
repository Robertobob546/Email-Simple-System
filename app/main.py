if __package__ in (None, ''):
    import sys
    from pathlib import Path

    # Make the project package available when running this file directly.
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.user import User


def main():
    tory = User('Tory')
    ramy = User('Ramy')        
    
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    
    ramy.check_inbox ()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox ()

    
if __name__ == '__main__':
    main()
