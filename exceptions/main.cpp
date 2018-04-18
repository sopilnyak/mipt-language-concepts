#include "SafeString.h"
#include "SafeFile.h"
#include "BadDestructor.h"

int main() {

    // Prints all prefixes of a string (calls recursive function)
    TRY(
            SafeString string {"string"};
            string.printPrefixes();
    )
            CATCH(Exception::E_InvalidParameterException, std::cerr << "Invalid Parameter!" << std::endl;)
    END

    // Try to open a file
    TRY(
            TRY(
                    SafeFile file("nosuchfile.txt");
    )
            // Don't catch anything, throw exception further
            END
    )
            CATCH(Exception::E_InvalidParameterException, std::cerr << "Will not be caught" << std::endl;)
            CATCH(Exception::E_FileNotFoundException, std::cerr << "File not found!" << std::endl;)
    END

    // Try to open a file without catching the exception
    TRY(
            SafeFile file("nosuchfile.txt");
    )
            CATCH(Exception::E_InvalidParameterException, std::cerr << "Will not be caught" << std::endl;)
    END

    // Throw exception from destructor
    TRY(
            BadDestructor file("nosuchfile.txt");
    )
    END

    return 0;
}
