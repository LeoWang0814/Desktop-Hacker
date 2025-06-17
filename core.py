import os
import shutil
import hashlib
import sys
SAFE = "ON"
RECOVERY = False

if SAFE == "ON":
    if os.name == "nt":
        desktop = os.path.join(os.environ["USERPROFILE"], "Desktop", "Fake Desktop")
    else:
        desktop = os.path.join(os.path.expanduser("~/Desktop"), "Fake Desktop")
else:
    if os.name == "nt":
        desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
    else:
        desktop = os.path.expanduser("~/Desktop")

if RECOVERY == False:
    innerError = False
    recoveryPos = os.path.join(desktop, hashlib.sha256(desktop.encode('utf-8')).hexdigest())
    if os.path.exists(recoveryPos):
        print('Please do not repeat the encryption, which will cause the files to fail to be decrypted.')
        input('Press Enter to confirm.')
        sys.exit()
    with open(recoveryPos, 'w') as f:
        def pour(targetPath):
            component = os.listdir(targetPath)
            for file in component:
                filePath = os.path.join(targetPath, file)
                if os.path.isdir(filePath):
                    f.write('D' + filePath + '?')
                    pour(filePath)
                elif filePath == recoveryPos:
                    continue
                else:
                    initialName = file
                    compName = (file + filePath)
                    hashName = hashlib.sha256(compName.encode('utf-8')).hexdigest()
                    try:
                        shutil.move(os.path.join(targetPath, file), os.path.join(desktop, hashName))
                    except Exception:
                        innerError = True
                        continue
                    recoveryLine = os.path.join(desktop, hashName) + "*" + filePath
                    f.write('F' + recoveryLine + '?')
        pour(desktop)
    component = os.listdir(desktop)
    if not(innerError):
        for file in component:
            filePath = os.path.join(desktop, file)
            if os.path.isdir(filePath):
                shutil.rmtree(filePath)
    print('Check Your Desktop ;)')
    input('Press Enter to confirm.')
else:
    recoveryPos = os.path.join(desktop, hashlib.sha256(desktop.encode('utf-8')).hexdigest())
    try:
        with open(recoveryPos, 'r') as f:
            recoveryCode = f.read()
    except Exception:
        print('CANNOT Find Recovery File.('+recoveryPos+')')
        print('Try to recover all the files in the Recycle Bin.')
        input('Press Enter to confirm.')
        sys.exit()
    splited = recoveryCode.split('?')
    recoveryDir = []
    recoveryFile = []
    switch = False
    for i in splited:
        if i == '':
            continue
        if i[0] == 'D':
            recoveryDir.append(i[1:])
        elif i[0] == 'F':
            recoveryFile.append(i[1:])
    for i in recoveryDir:
        try:
            os.makedirs(i)
        except Exception:
            pass
    errors = [[],[]]
    fail = False
    for i in recoveryFile:
        operation = i.split('*')
        try:
            if os.path.exists(operation[1]):
                print(operation[1] + 'Exists.')
                errors[1].append(operation[1] + '(After encryption:' + operation[0] + ')')
                fail = True
            else:
                shutil.move(operation[0], operation[1])
                print('Recovered:'+operation[1])
        except FileNotFoundError:
            print('CANNOT Find'+operation[1])
            errors[0].append(operation[1]+'(After encryption:'+operation[0]+')')
            fail = True

    os.remove(recoveryPos)
    if fail:
        print('CANNOT RECOVER:')
        print('--------------------')
        if len(errors[0]) != 0:
            [print(i) for i in errors[0]]
            print('Because we cannot find the encrypted files')
            print('--------------------')
        if len(errors[1]) != 0:
            [print(i) for i in errors[1]]
            print('Because these files already exist.')
            print('--------------------')
        print('Please manually rename the file and place it in the correct location according to the error message.')
        print('--------------------')
        with open(os.path.join(desktop, 'Recovery Hint.txt'), 'w') as file:
            file.write('CANNOT RECOVER:\n')
            file.write('--------------------\n')
            if len(errors[0]) != 0:
                [file.write(i+'\n') for i in errors[0]]
                file.write('Because we cannot find the encrypted files\n')
                file.write('--------------------\n')
            if len(errors[1]) != 0:
                [file.write(i+'\n') for i in errors[1]]
                file.write('Because these files already exist.\n')
                file.write('--------------------\n')
            file.write(
                'Please manually rename the file and place it in the correct location according to the error messages.\n')
            file.write('--------------------\n')
        print('All of the above error messages have been saved to a file named Recovery Hint.txt on your desktop.')
        input('Press Enter to confirm.')
    else:
        print('Recovered Successfully :)')
        input('Press Enter to confirm.')