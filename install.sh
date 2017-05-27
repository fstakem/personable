dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Arguments
install_env=$1

echo "Install python libs for env:" $install_env

pyenv=`ls -d */ | grep *env | xargs`

if [[ -z pyenv ]]; then
    exit 1;
fi

echo "Using virtual env:" $pyenv

if [ $install_env = "dev" ]; then
    pip-compile ./requirements/base.in
    pip-sync ./requirements/base.txt
    pip-compile ./requirements/dev.in
    pip-sync ./requirements/dev.txt
elif [ $install_env = "prod" ]; then
    pip-compile ./requirements/base.in
    pip-sync ./requirements/base.txt
    pip-compile ./requirements/prod.in
    pip-sync ./requirements/prod.txt
else
    exit 1;
fi
