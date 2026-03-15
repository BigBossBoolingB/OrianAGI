
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python311
    python311Packages.pip
    python311Packages.flask
    python311Packages.numpy
    python311Packages.biopython
  ];
}
