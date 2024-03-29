"""Module docstring for Device Unde Test"""

class DUT:
    def __init__(self):
        """
        DUT -> type of device,
               properties of device,
               measurements to perform -> (IV,CV),
        OUTPUT -> IV characteristics
               -> CV characteristics
               -> file? a la SPICE/BSIM?
        """
        pass

    def output(self,
               fn: str="output",
               ft: str="",
               dest: str="./")-> str:
        """Writes the output to a file of specified type.

        Parameters
        ----------
        fn : str, optional
            file name, by default "output"
        ft : str, optional
            file type (such as .txt or .csv or .data), by default ""
        dest : str, optional
            destination folder, by default "./"

        Returns
        -------
        str
            "Success" or "Failure"
        """
        fp = dest + fn + ft
        try:
            import datetime as dt
            with open(fp,'w') as f:
                '''
                write to file
                '''
                f.write("#Output File generated by semicpy.characterization.dut.DUT\n")
                f.write("#Date: %s\n\n" % dt.datetime.now())
                f.write("----------------------------------\n")
                f.write("Leff:\t%s\tm\n")
            return "Success"
        except (IOError,OSError):
            print("Error opening file!")
            return "Failure"
