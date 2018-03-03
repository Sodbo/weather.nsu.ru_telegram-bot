conda env export --file env.yml
conda env update -f env.yml
git add env.yml
git commit -m 'updated env.yml'
