#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <signal.h>
#include <stdlib.h>

/**
 * infinite_while - runs an infinite while loop
 *
 * Return: nothing
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - creates 5 zombie processes
 *
 * Return: an integer
 */
int main(void)
{
	pid_t pid;
	int i;

	pid = fork();

	for (i = 0; i < 4; i++)
	{
		if (pid <= 0)
			break;
		pid = fork();
		if (pid > 0)
			printf("Zombie process created, PID: %i\n", pid);
	}
	if (pid <= 0)
		exit(0);
	infinite_while();
	return (0);
}
