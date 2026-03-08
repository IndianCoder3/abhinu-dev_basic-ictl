# Chapter 2: Getting Started - Setup and First Steps

Great! You have ICTL installed (or your teacher gave it to you). Now let's make sure everything is ready to code!

## Testing That ICTL Works

Let's check if ICTL is ready to go.

### Step 1: Open a Terminal

A **terminal** is like a text-based control room for your computer. It lets you run programs by typing commands.

**On Windows:**
- Press `Windows key + R`
- Type `cmd` and press Enter
- A black window appears - that's your terminal!

**Or easier:**
- Go to your folder
- Right-click in an empty space
- Choose "Open in Terminal"

### Step 2: Test ICTL

Type this and press Enter:

```bash
ictl
```

You should see something like:
```
========================================
ICTL Interpreter - Interactive Shell
========================================
Type 'exit' to quit
>
```

**Perfect!** ICTL is working! Type `exit` and press Enter to leave.

If you see "ictl is not recognized," it means ICTL might not be in the right path. Ask your teacher or admin for help setting it up.

## Interactive Shell vs. Script Files

There are two ways to use ICTL:

### 1. Interactive Shell (For Quick Testing)

This is where you type commands one at a time:

```bash
ictl
> Terminal.Echo("Hello!")
Hello!
>
```

Great for experimenting!

### 2. Script Files (For Real Programs)

This is where you write a whole program in a file and run it. (This is what we'll do!)

## Creating Your First Folder

Let's create a place to store your ICTL programs.

### Easy Steps:

1. **Find a good spot** on your computer (like Desktop or Documents)
2. **Right-click** in empty space
3. **Click "New Folder"**
4. **Name it** something like `MyICTLPrograms` or `ICTL_Fun`
5. **Open this folder** by double-clicking it

**Important:** Remember where this folder is! You'll create all your ICTL files here.

## Creating Your First ICTL File

Now let's create an ICTL program!

### Step 1: Open Notepad

**Easy way:**
1. Click the Windows Start button
2. Type `notepad`
3. Click on "Notepad"

A blank text document appears.

### Step 2: Write Some Code

Copy and paste this into Notepad:

```ictl
Program.Main {
    Terminal.Echo("Hello, World!")
}
```

Or just type it if you want to practice!

### Step 3: Save the File

1. Press `Ctrl+S` (or go to File > Save)
2. A "Save" window appears
3. **Important:** 
   - Navigate to your `MyICTLPrograms` folder
   - Name the file: `hello.ictl` (must end with `.ictl`)
   - Make sure the file type says "All Files" (not "Text Files")
4. Click "Save"

**You just created your first ICTL program!** 🎉

## Running Your ICTL Program

Time to see your program work!

### Step 1: Open Terminal in Your Folder

1. **Open your `MyICTLPrograms` folder** (where you saved `hello.ictl`)
2. **Right-click in empty space** (not on the file)
3. **Click "Open in Terminal"**

A terminal window appears, and you should be in your folder.

### Step 2: Run Your Program

Type this command and press Enter:

```bash
ictl hello.ictl
```

You should see:
```
Hello, World!
```

**Boom! You just ran your first program!** 🚀

### What Happened?

1. You typed `ictl hello.ictl`
2. ICTL read your file
3. ICTL ran your code
4. Your code printed "Hello, World!"
5. Done!

## Troubleshooting

### Problem: "ictl is not recognized"

**Solution:** Your ICTL might not be set up correctly. Ask your teacher or the person who installed ICTL to help you.

### Problem: "File not found"

**Solution:** Make sure:
- Your file is saved as `hello.ictl` (check the filename!)
- You opened the terminal in the same folder as your file
- The folder shows `hello.ictl` when you view its contents

### Problem: "Syntax Error" or other error

Don't worry! Programming errors happen all the time. ICTL will tell you what went wrong. We'll learn how to fix errors in later chapters!

### Problem: No "Open in Terminal" visible

It means Terminal wasn't installed. In this case:
- Open the Start Menu
- Type CMD
- Press Enter
- Go back to File Explorer
- 


## Quick Testing with Interactive Shell

Before you write a whole program, you can test ICTL commands quickly!

### Try It:

1. **Open terminal** (anywhere)
2. **Type:** `ictl`
3. **You'll see:** `>`

Now type commands one at a time:

```
> Terminal.Echo("I'm learning ICTL!")
I'm learning ICTL!
> Terminal.Echo("This is cool!")
This is cool!
> exit
```

The `>` means ICTL is waiting for your command. Each command runs instantly!

**Perfect for experimenting without creating files!**

## Recommended Text Editors

You can write ICTL code in any text editor. Here are some options:

### Option 1: Notepad (Already on your computer!)

- ✅ Super simple
- ✅ No setup needed
- ⚠️ No special help for coding

### Option 2: Notepad++

- ✅ Free
- ✅ Better for coding
- ✅ Easy to download from notepad-plus-plus.org (only with permission!)

### Option 3: VS Code (Professional but easy)

- ✅ Free
- ✅ Super powerful
- ✅ Great for learning
- Download from: code.visualstudio.com (again, only with permission!)

For now, **Notepad is perfectly fine!** Start there and upgrade later if you want.

## You're Ready!

Congratulations! You're all set up! 

You now have:
✅ ICTL installed and working
✅ A folder for your programs
✅ A text editor to write code
✅ A way to run your programs

---

## Next Steps

Ready to write your first real program? Go to **Chapter 3: Your First ICTL Program!**
