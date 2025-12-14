# For developers on NixOS
# Developers on other OSes may ignore this file
with import <nixpkgs> {};
let
  blue = "\\e[0;94m";
  green = "\\e[0;32m";
  yellow ="\\e[0;33m";
  red = "\\e[1;31m";
  reset="\\e[0m";
in
pkgs.mkShell {
  name = "fpsupport";
  NIX_LD_LIBRARY_PATH = lib.makeLibraryPath [
    stdenv.cc.cc
    enchant
  ];

  NIX_LD = lib.fileContents "${stdenv.cc}/nix-support/dynamic-linker";

  packages = with pkgs; [
    python312
    poetry
  ];

  shellHook = ''
     export LD_LIBRARY_PATH=$NIX_LD_LIBRARY_PATH

     branch=$(git status 2>/dev/null | grep 'On branch' | sed 's/On branch //')
     dc="${blue}"
     rs="${reset}"
     if [ "$branch" == "main" ]; then
        bc="${red}"
     elif [ "$branch" == "develop" ]; then
        bc="${yellow}"
     else
        bc="${green}"
     fi
     dir=$(pwd | sed 's/.*\(fpsupport\)/\1/')

     export PS1="$dc\nnix-shell:…/\$dir: $bc$branch$rs\n> "
   '';
}

