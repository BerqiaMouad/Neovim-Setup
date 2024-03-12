-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here
--

HOME = os.getenv("HOME")

-- function to open a floating terminal and run a command
local function open_terminal_and_run(cmd)
  vim.cmd("ToggleTerm direction=float")
  vim.cmd("term " .. cmd)
end
vim.keymap.set("n", "<space>term", function()
  open_terminal_and_run("")
end, { desc = "Open floating [term]inal" })

-- ================== CODEFORCES STUFF !! ====================================

-- function to test solution against sample tests in a floating terminal
local function codeforces_test()
  -- Get the current buffer filename
  local filename = vim.api.nvim_buf_get_name(0)

  -- Check if filename exists (optional)
  if not filename then
    vim.notify("Error: No file open!")
    return
  end

  -- Run test.py with the filename as argument in a floating terminal
  open_terminal_and_run("python3 " .. HOME .. "/.config/nvim/mouad_codeforces_tool/test.py " .. filename)
end

vim.keymap.set("n", "<space>test", codeforces_test, { desc = "Test the current problem." })

-- -----------------------------------------------------------------------------------

-- function to create contest with given contest id and programming language
local function codeforces_create_contest()
  -- Get contest ID and language from user input
  local contest_id = vim.fn.input("Enter contest ID: ")

  -- Validate input
  if not contest_id or not vim.fn.executable("python3") then
    print("Invalid input or python3 not found.")
    return
  end

  -- Execute the Python script
  local python_command =
    string.format("python3 %s/.config/nvim/mouad_codeforces_tool/create_contest.py %s", HOME, contest_id)
  vim.fn.jobstart(python_command, {
    print("Creating Contest..."),
    on_exit = function(_, exit_code, output_errors)
      if exit_code == 0 then
        print("Contest created successfully!")
        vim.api.nvim_command(":cd " .. contest_id)
      else
        print("Error creating contest.")
        print(output_errors)
      end
    end,
  })
end

vim.keymap.set("n", "<space>cp", codeforces_create_contest, { desc = "Create Codefroces Contest." })

-- --------------------------------------------------------------------------------------
local function codeforces_create_problem_file()
  local problem_name = vim.fn.input("Enter Problem Name: ")
  local lang = vim.fn.input("Enter Programming Language (cpp/python): ")

  if not problem_name or not vim.fn.executable("python3") then
    print("Invalid input or python3 not found.")
  end

  local python_command = string.format(
    "python3 %s/.config/nvim/mouad_codeforces_tool/create_problem_file.py %s %s",
    HOME,
    problem_name,
    lang
  )
  vim.fn.jobstart(python_command, {
    print(string.format("Creating Problem %s %s File...", problem_name, lang)),
    on_exit = function(_, exit_code, output_errors)
      if exit_code == 0 then
        print(string.format("%s file for problem %s created successfully!", lang, problem_name))
      else
        print("Error creating file.")
        print(output_errors)
      end
    end,
  })
end

vim.keymap.set("n", "<space>cpf", codeforces_create_problem_file, { desc = "Create Problem file (cpp/python)." })

-- --------------------------------------------------------------------------------------------------------------------

local function codeforces_submit()
  local problem_name = vim.fn.input("Enter Problem Name: ")
  local lang = vim.fn.input("Enter Programming Language (cpp/python): ")

  if not problem_name or not vim.fn.executable("python3") then
    print("Invalid input or python3 not found.")
  end

  local python_command =
    string.format("python3 %s/.config/nvim/mouad_codeforces_tool/submit.py %s %s", HOME, problem_name, lang)

  vim.fn.jobstart(python_command, {
    print(string.format("Submitting Problem %s...", problem_name)),
    on_exit = function(_, exit_code, output_errors)
      if exit_code == 0 then
      else
        vim.notify("Error submitting!", "error")
        vim.notify(output_errors, "error")
      end
    end,
    on_stdout = function(_, data, _)
      local text = data[1]
      if string.find(text, "Accepted") ~= nil then
        vim.notify(text, "info")
      else
        vim.notify(text, "error")
      end
    end,
  })
end

vim.keymap.set("n", "<space>sub", codeforces_submit, { desc = "Submit Solution to codeforces." })

-- ================== CODEFORCES STUFF !! ====================================
