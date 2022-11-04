solutions = [
  { "name"        : 'src',
    "url"         : 'https://github.com/rebeccasf/chromium.src.git@origin/nw65',
    "deps_file"   : 'DEPS',
    "managed"     : True,
    "custom_deps" : {
      "src/third_party/WebKit/LayoutTests": None,
      "src/chrome_frame/tools/test/reference_build/chrome": None,
      "src/chrome_frame/tools/test/reference_build/chrome_win": None,
      "src/chrome/tools/test/reference_build/chrome": None,
      "src/chrome/tools/test/reference_build/chrome_linux": None,
      "src/chrome/tools/test/reference_build/chrome_mac": None,
      "src/chrome/tools/test/reference_build/chrome_win": None,
    },
    "custom_vars": {},
  },
]
